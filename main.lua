function scandir(directory)
    local i, table, popen = 0, {}, io.popen
    local pfile = popen('dir "'..directory..'" /b')
    for filename in pfile:lines() do
        i = i + 1
        table[i] = filename
    end
    pfile:close()
    return table
end

function love.load()
    font = love.graphics.newFont(96)
    path = "..\\"
    folder = scandir(path)
    counter = 0
    timer = 0
 end

 function love.update(dt)
    timer = timer + dt
    if timer > 2 then
        counter = 0
        folder = scandir(path)
        for i,file in ipairs(folder) do
            if string.match(file, "%a*V1_%d+") then
                counter = counter + 1
            end
        end
        timer = 0
    end
 end

 function love.draw()
    love.graphics.setFont(font)
    love.graphics.print(counter, 64, 0)
    -- love.graphics.print(timer, 0, 90)
    -- folder[1] folder[2] 
    -- love.graphics.print(folder, 0, 10)
end

