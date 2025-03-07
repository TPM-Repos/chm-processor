Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Initialize Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IView Interface](topic534.md) : Initialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_environment_
    The view's environment.

Glossary Item Box

Initializes the view. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Initialize( _
       ByVal _environment_ As [IViewEnvironment](topic549.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IView](topic534.md)
    Dim environment As [IViewEnvironment](topic549.md)
     
    instance.Initialize(environment)  
  
C#|   
---|---  
      
    
    void Initialize( 
       [IViewEnvironment](topic549.md) _environment_
    )  
  
#### Parameters

 _environment_
    The view's environment.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IView Interface](topic534.md)   
[IView Members](topic535.md)


