Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Initialize Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [IApplicationPlugin Interface](topic2004.md) : Initialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The application which is hosting the DriveWorks API.

Glossary Item Box

Initializes the plugin. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Initialize( _
       ByVal _application_ As [IApplication](topic24.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationPlugin](topic2004.md)
    Dim application As [IApplication](topic24.md)
     
    instance.Initialize(application)  
  
C#|   
---|---  
      
    
    void Initialize( 
       [IApplication](topic24.md) _application_
    )  
  
#### Parameters

 _application_
    The application which is hosting the DriveWorks API.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplicationPlugin Interface](topic2004.md)   
[IApplicationPlugin Members](topic2005.md)


