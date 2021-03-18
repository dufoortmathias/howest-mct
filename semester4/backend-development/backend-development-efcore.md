# Herhalingsoefening stappen

## Opzetten van nieuw project
* Aanmaken Git project en lokaal clonen
* Nieuw project aanmaken:  `dotnet new webapi`
* Builden: `dotnet build`
* Test of dit werkt
* Docker opzetten: ctrl+shift+P => add docker files to workspace
* docker-compose.yml aanpassen voor SQL server:

```
version: "3.9"

services:
    db:
        image: "mcr.microsoft.com/mssql/server:2017-CU22-ubuntu-16.04"
        environment:
            SA_PASSWORD: "<YourNewStrong@Passw0rd>"
            ACCEPT_EULA: "Y"
        ports:
            - 1433:1433
        volumes:
            - ../db/data:/var/opt/mssql/data
    api:
        image: <CHANGE-THIS>
        build:
            context: .
            dockerfile: ./Dockerfile
        environment:
            - ASPNETCORE_URLS=http://+:5000
            - ASPNETCORE_ENVIRONMENT=Docker
        ports:
            - 5000:5000
            - 5001:5000
        depends_on:
            - db
        volumes:
            - ~/.vsdbg:/remote_debugger:rw
```

* Test SQL server via Docker: 
    * `docker-compose up --build`
    * In Azure data studio:
        1. Create a connection
        2. Server = `localhost`
        3. username = `sa`
        4. Password = zie `docker-compose.yml`
        5. Connect
    * Create a new database:
        1. New query
        2. `CREATE DATABASE sneakers`
* Meerdere appsettings files maken: `appsettings.json, appsettings.Docker.json, appsettings.Development.json`
* Configuratie opzetten voor `ASP.NET`
* Connectionstrings:
    * Configuration folder aanmaken
    * Class ConnectionStrings met daarin 1 property: `public string SQL {get; set;}`
    * Voeg `services.Configure<ConnectionStrings>(...)` toe in `Startup.cs` 

## EF Core Context aanmaken

* Nuget packages installeren:
    * `dotnet add package Microsoft.EntityFrameworkCore.Design`
    * `dotnet add package Microsoft.EntityFrameworkCore.SqlServer`
    * `dotnet build` om IntelliSense weer te laten werken met de nieuwe packages
    * Als IntelliSense nog niet werkt: ctrl+shift+P => Restart OmniSharp
* EF Core Context aanmaken:
    * Data map aanmaken
    * Create Context class, bv: RegistrationContext
    * ConnectionStrings field aanmaken 
    * Constructor aanmaken:
    ```
    public RegistrationContext(
            DbContextOptions<RegistrationContext> options, 
            IOptions<ConnectionStrings> connectionStrings
    ) : base(options)
        {
            _connectionStrings = connectionStrings.Value;
        }
    ```
    * `OnConfiguring` method (zie vorige labo's voor code)
    * `OnModelCreating` method (zie vorige labo's voor code)
    
    * `DbSet<Model>` fields aanmaken voor elk `Model`


## Modellen aanmaken

* Models map
* Voor elk model een klasse
* In elke klasse de props voor het model

## Seeding klaarzetten

* Aanmaken van data in de OnModelCreating klasse
* Zie vorige labo's voor voorbeelden


## Migratie testen en controleren of aangemaakt

* context toevoegen in `Startup.cs` met `AddDbContext<IContext, Context>()`
* `docker-compose up --build`
* `dotnet ef migrations add "first migration"`
* `dotnet ef database update`
* Kijk in Azure Data Studio of de data is aangemaakt

## Controller toevoegen

* Nieuwe klasse in Controller map
* Extends ControllerBase
* Constructor
* HTTP methods: [HttpGet]

## Actions maken/services/repo of eerst repo/service en dan alles aanroepen vanuit de context

* `services.AddTransient<Interface, Class>();` voor elke repository en service

## Indien je swagger wil gebruiken

Voeg dan deze code toe in startup.cs

```cs
if (env.IsDevelopment() || env.IsEnvironment("Docker")) {
    app.UseDeveloperExceptionPage();
    app.UseSwagger();
    app.UseSwaggerUI(c => c.SwaggerEndpoint("/swagger/v1/swagger.json", "Sneakers.API v1"));
}
```

Deze code staat er standaard al voor een deel, maar `env.IsEnvironment("Docker")` voeg je nog toe.