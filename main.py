"""
Sistema GoodWe de Automação Inteligente
FIAP - Sprint 3 - 2025

Equipe:
- Auro Vanetti (RM: 563761)
- Enzo H. K. Nishida (RM: 565052)
- Francisco B. N. Neto (RM: 565868)
- Kaio Correa (RM: 563443)
- Renan Mano Otero (RM: 554911)
"""

import time
import random
from datetime import datetime

class GoodWeAutomationSystem:
    
    def __init__(self):
        self.solar_generation = 3.2
        self.home_consumption = 2.1
        self.battery_level = 75
        self.energy_source = "solar"
        self.devices = {
            "luz_sala": True,
            "ar_condicionado": False,
            "geladeira": True,
            "tv": True
        }
        self.auto_mode = True
        self.event_log = []
        print("✅ Sistema GoodWe inicializado!")
        self.log_event("Sistema iniciado")
    
    def log_event(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.event_log.append({"time": timestamp, "msg": message})
        print(f"[{timestamp}] {message}")
    
    def read_goodwe_inverter(self):
        variation = random.uniform(-0.5, 0.5)
        self.solar_generation = max(0.5, min(4.5, self.solar_generation + variation))
        return self.solar_generation
    
    def read_iot_sensors(self):
        variation = random.uniform(-0.3, 0.3)
        self.home_consumption = max(0.8, min(3.5, self.home_consumption + variation))
        return self.home_consumption
    
    def calculate_surplus(self):
        return round(self.solar_generation - self.home_consumption, 2)
    
    def decision_algorithm(self):
        surplus = self.calculate_surplus()
        
        if surplus > 0.5 and self.battery_level < 90:
            self.battery_level = min(100, self.battery_level + 0.5)
            self.energy_source = "solar"
            if random.random() > 0.95:
                self.log_event(f"✓ Carregando bateria ({surplus:.2f} kW excedente)")
        
        elif surplus < -0.3 and self.battery_level > 20:
            self.battery_level = max(0, self.battery_level - 0.3)
            self.energy_source = "bateria"
            if random.random() > 0.95:
                self.log_event(f"⚡ Usando bateria ({self.battery_level:.1f}%)")
        
        elif self.battery_level < 15:
            self.energy_source = "rede"
            self.log_event(f"⚠ Bateria baixa - mudando para rede")
        
        else:
            self.energy_source = "solar"
        
        return self.energy_source
    
    def smart_device_control(self):
        surplus = self.calculate_surplus()
        hour = datetime.now().hour
        
        if surplus < -0.8 and hour >= 18:
            if self.devices["ar_condicionado"]:
                self.devices["ar_condicionado"] = False
                self.log_event("🤖 Alexa: Desligando ar-condicionado")
    
    def print_dashboard(self):
        status = {
            "solar": round(self.solar_generation, 2),
            "consumo": round(self.home_consumption, 2),
            "bateria": round(self.battery_level, 1),
            "surplus": self.calculate_surplus(),
            "fonte": self.energy_source,
            "eficiencia": round((self.solar_generation / 4.5) * 100, 0)
        }
        
        print("\n" + "="*60)
        print("⚡ SISTEMA GOODWE - DASHBOARD")
        print("="*60)
        print(f"🌞 Geração Solar:  {status['solar']:.2f} kW ({status['eficiencia']:.0f}%)")
        print(f"🏠 Consumo Casa:   {status['consumo']:.2f} kW")
        print(f"🔋 Bateria:        {status['bateria']:.1f}%")
        print(f"⚡ Balanço:        {status['surplus']:+.2f} kW")
        print(f"🔌 Fonte:          {status['fonte'].upper()}")
        print("-"*60)
        print("📱 Dispositivos:")
        for device, state in self.devices.items():
            icon = "✅" if state else "❌"
            print(f"   {icon} {device.replace('_', ' ').title()}")
        print("="*60)
        
        if self.event_log:
            print("\n📋 Últimos eventos:")
            for event in self.event_log[-3:]:
                print(f"   [{event['time']}] {event['msg']}")
        print()
    
    def run_cycle(self):
        self.read_goodwe_inverter()
        self.read_iot_sensors()
        if self.auto_mode:
            self.decision_algorithm()
            self.smart_device_control()
    
    def run(self, cycles=None):
        print("\n🚀 Sistema iniciado!")
        print("📊 Monitorando energia solar...\n")
        
        cycle_count = 0
        try:
            while cycles is None or cycle_count < cycles:
                self.run_cycle()
                
                if cycle_count % 10 == 0:
                    self.print_dashboard()
                
                cycle_count += 1
                time.sleep(2)
        
        except KeyboardInterrupt:
            print("\n\n⏹️  Sistema encerrado")
            self.print_dashboard()

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║        SISTEMA GOODWE DE AUTOMAÇÃO INTELIGENTE          ║
    ║                                                          ║
    ║              Sprint 3 - Protótipo Funcional             ║
    ║                      FIAP 2025                          ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    
    Equipe:
    • Auro Vanetti (RM: 563761)
    • Enzo H. K. Nishida (RM: 565052)
    • Francisco B. N. Neto (RM: 565868)
    • Kaio Correa (RM: 563443)
    • Renan Mano Otero (RM: 554911)
    """)
    
    system = GoodWeAutomationSystem()
    system.run(cycles=15)  # Roda por 30 segundos
    
    print("\n✅ Demonstração concluída!")
    print(f"📊 Total de eventos: {len(system.event_log)}")
