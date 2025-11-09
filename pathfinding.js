import { Vec3 } from 'vec3';

export class Pathfinder {
  constructor(bot) {
    this.bot = bot;
    this.target = null;
    this.isMoving = false;
    this.followTarget = null;
  }

  distance(pos1, pos2) {
    const dx = pos1.x - pos2.x;
    const dy = pos1.y - pos2.y;
    const dz = pos1.z - pos2.z;
    return Math.sqrt(dx * dx + dy * dy + dz * dz);
  }

  async goToPosition(targetPos, minDistance = 2) {
    if (!targetPos || !this.bot.position) return false;

    this.target = targetPos;
    this.isMoving = true;

    const moveInterval = setInterval(() => {
      if (!this.isMoving || !this.target) {
        clearInterval(moveInterval);
        return;
      }

      const distance = this.distance(this.bot.position, this.target);
      
      if (distance <= minDistance) {
        this.stop();
        clearInterval(moveInterval);
        return;
      }

      const direction = {
        x: this.target.x - this.bot.position.x,
        y: this.target.y - this.bot.position.y,
        z: this.target.z - this.bot.position.z
      };

      const horizontalDist = Math.sqrt(direction.x * direction.x + direction.z * direction.z);
      
      if (horizontalDist > 0) {
        direction.x /= horizontalDist;
        direction.z /= horizontalDist;
      }

      const speed = 0.1;
      const movement = {
        x: direction.x * speed,
        y: 0,
        z: direction.z * speed
      };

      if (direction.y > 1) {
        this.bot.jump = true;
      }

      this.bot.moveDirection = movement;
      
      const yaw = Math.atan2(-direction.x, direction.z);
      const pitch = -Math.atan2(direction.y, horizontalDist);
      
      this.bot.lookAt(yaw, pitch);

    }, 50);

    return new Promise(resolve => {
      const checkInterval = setInterval(() => {
        if (!this.isMoving) {
          clearInterval(checkInterval);
          resolve(true);
        }
      }, 100);
    });
  }

  startFollowing(playerName) {
    this.followTarget = playerName;
    
    const followInterval = setInterval(() => {
      if (!this.followTarget) {
        clearInterval(followInterval);
        return;
      }

      const player = this.getPlayerPosition(this.followTarget);
      if (player) {
        const distance = this.distance(this.bot.position, player);
        if (distance > 3) {
          this.goToPosition(player, 2);
        }
      }
    }, 1000);
  }

  stopFollowing() {
    this.followTarget = null;
    this.stop();
  }

  getPlayerPosition(playerName) {
    if (this.bot.players && this.bot.players[playerName]) {
      return this.bot.players[playerName].position;
    }
    return null;
  }

  stop() {
    this.isMoving = false;
    this.target = null;
    if (this.bot.moveDirection) {
      this.bot.moveDirection = { x: 0, y: 0, z: 0 };
    }
  }
}
