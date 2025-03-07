Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Initialize Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IGroupConnector Interface](topic1706.md) : Initialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The application that the connector is in.

Glossary Item Box

Called after creating a new instance, this should be responsible for setting up the connector to its context. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Initialize( _
       ByVal _application_ As [IApplication](topic24.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupConnector](topic1706.md)
    Dim application As [IApplication](topic24.md)
     
    instance.Initialize(application)  
  
C#|   
---|---  
      
    
    void Initialize( 
       [IApplication](topic24.md) _application_
    )  
  
#### Parameters

 _application_
    The application that the connector is in.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupConnector Interface](topic1706.md)   
[IGroupConnector Members](topic1707.md)


