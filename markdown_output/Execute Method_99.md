Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Execute Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [RunDriveAppTask Class](topic1942.md) : Execute Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The application that created the connector.

Glossary Item Box

Runs the DriveApp using the alias name specified in the arguments property. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Execute( _
       ByVal _application_ As [IApplication](topic24.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RunDriveAppTask](topic1942.md)
    Dim application As [IApplication](topic24.md)
     
    instance.Execute(application)  
  
C#|   
---|---  
      
    
    public void Execute( 
       [IApplication](topic24.md) _application_
    )  
  
#### Parameters

 _application_
    The application that created the connector.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RunDriveAppTask Class](topic1942.md)   
[RunDriveAppTask Members](topic1943.md)


