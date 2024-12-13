import pygame
import random
from ..agents.birds import Birds


class CrowdSimulation:
    def __init__(self, num_agents, agent_type, screen):
        self.agents = []
        self.num_agents = num_agents
        self.agent_type = agent_type
        self.screen = screen

    def create_agents(self):
        """Crée les agents selon le type spécifié."""
        for _ in range(self.num_agents):
            if self.agent_type == "birds":
                agent = Birds(
                    random.randint(0, 800), random.randint(0, 600),
                    self.screen
                )
                self.agents.append(agent)

    def update(self):
        """Met à jour les positions des agents."""
        for agent in self.agents:
            agent.update(self.screen.get_width(), self.screen.get_height())

    def draw(self, screen):
        """Dessine chaque agent."""
        for agent in self.agents:
            if hasattr(agent, "draw"):
                agent.draw(screen)
