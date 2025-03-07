Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Initialize Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [IApplicationModule Interface](topic1997.md) : Initialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The application which is hosting the DriveWorks API.

Glossary Item Box

Initializes the module. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Initialize( _
       ByVal _application_ As [IApplication](topic24.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationModule](topic1997.md)
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

[IApplicationModule Interface](topic1997.md)   
[IApplicationModule Members](topic1998.md)


