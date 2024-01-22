MAXDIS = 10000

class Entity:
    def __init__(self, maxHp, v):
        self.maxHp = maxHp
        self.hp = maxHp
        self.effects = []
        self.speed = v
        self.distance = MAXDIS

    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, heal):
        self.hp += heal
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def isAlive(self):
        return self.hp > 0
    
    # 为了方便大家理解，这里采用了跳秒的方式，实际实现的时候一定是离散的，直接跳到下一次行动
    def tick(self):
        self.distance -= self.speed
        if self.distance <= 0:
            self.distance = MAXDIS
            return True
        return False
    

class Player(Entity):
    pass



class Enemy(Entity):
    pass


if __name__ == "__main__":
    player = Player(100, 100)
    enemy = Enemy(50, 70)

    while player.isAlive() and enemy.isAlive():
        playerMoved = False
        enemyMoved = False
        if player.tick():
            enemy.takeDamage(10)
            playerMoved = True
        if enemy.tick():
            player.takeDamage(10)
            enemyMoved = True

        if playerMoved and enemyMoved:
            print("本次双方同时行动，玩家剩余血量：", player.hp, "距离下次行动还有：", player.distance, "敌人剩余血量：", enemy.hp, "距离下次行动还有：", enemy.distance)
        elif playerMoved:
            print("玩家行动，玩家剩余血量：", player.hp, "距离下次行动还有：", player.distance, "敌人剩余血量：", enemy.hp, "距离下次行动还有：", enemy.distance)
        elif enemyMoved:
            print("敌人行动，玩家剩余血量：", player.hp, "距离下次行动还有：", player.distance, "敌人剩余血量：", enemy.hp, "距离下次行动还有：", enemy.distance)


        
    
