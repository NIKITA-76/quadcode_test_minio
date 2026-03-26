ENV['VAGRANT_DEFAULT_PROVIDER'] = 'virtualbox'

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024" #1gb ram
    vb.cpus = 1 #1 core
  end

  config.vm.define "vm1" do |vm1|
    vm1.vm.hostname = "vm1"
    vm1.vm.network "private_network", ip: "192.168.56.11"
    vm1.vm.provider "virtualbox" do |vb|
      vb.customize ["createmedium", "disk",
        "--filename", "vm1-minio-disk.vdi", #подключаем диск как файл
        "--size", "3120"] 
      vb.customize ["storageattach", :id,
        "--storagectl", "SCSI", #Серверный тип подключения
        "--port", "2",
        "--device", "0",
        "--type", "hdd",
        "--medium", "vm1-minio-disk.vdi",
        "--nonrotational", "on"] #Говорим что не крутилки
    end
  end

  config.vm.define "vm2" do |vm2|
    vm2.vm.hostname = "vm2"
    vm2.vm.network "private_network", ip: "192.168.56.12"
    vm2.vm.provider "virtualbox" do |vb|
      vb.customize ["createmedium", "disk",
        "--filename", "vm2-minio-disk.vdi",
        "--size", "3120"]
      vb.customize ["storageattach", :id,
        "--storagectl", "SCSI",
        "--port", "2",
        "--device", "0",
        "--type", "hdd",
        "--medium", "vm2-minio-disk.vdi",
        "--nonrotational", "on"]
    end
  end

  config.vm.define "vm3" do |vm3|
    vm3.vm.hostname = "vm3"
    vm3.vm.network "private_network", ip: "192.168.56.13"
    vm3.vm.provider "virtualbox" do |vb|
      vb.customize ["createmedium", "disk",
        "--filename", "vm3-minio-disk.vdi",
        "--size", "3120"]
      vb.customize ["storageattach", :id,
        "--storagectl", "SCSI",
        "--port", "2",
        "--device", "0",
        "--type", "hdd",
        "--medium", "vm3-minio-disk.vdi",
        "--nonrotational", "on"]
    end
  end

end
