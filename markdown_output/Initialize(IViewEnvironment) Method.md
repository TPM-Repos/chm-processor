Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Initialize(IViewEnvironment) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ViewControl Class](topic1119.md) > [Initialize Method](topic1135.md) : Initialize(IViewEnvironment) Method  
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
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Overloads Sub Initialize( _
       ByVal _environment_ As [IViewEnvironment](topic549.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ViewControl](topic1119.md)
    Dim environment As [IViewEnvironment](topic549.md)
     
    instance.Initialize(environment)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public void Initialize( 
       [IViewEnvironment](topic549.md) _environment_
    )  
  
#### Parameters

 _environment_
    The view's environment.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ViewControl Class](topic1119.md)   
[ViewControl Members](topic1120.md)   
[Overload List](topic1135.md)


