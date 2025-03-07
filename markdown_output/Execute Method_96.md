Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Execute Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IScheduleConnectorTask Interface](topic1734.md) : Execute Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The application that the created the connector.

Glossary Item Box

Called to execute the task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Execute( _
       ByVal _application_ As [IApplication](topic24.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IScheduleConnectorTask](topic1734.md)
    Dim application As [IApplication](topic24.md)
     
    instance.Execute(application)  
  
C#|   
---|---  
      
    
    void Execute( 
       [IApplication](topic24.md) _application_
    )  
  
#### Parameters

 _application_
    The application that the created the connector.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IScheduleConnectorTask Interface](topic1734.md)   
[IScheduleConnectorTask Members](topic1735.md)


