Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Initialize Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ICaptureView Interface](topic13347.md) : Initialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_env_
    The environment of the view.

Glossary Item Box

Initializes the capture view. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Initialize( _
       ByVal _env_ As [ICaptureViewEnvironment](topic13353.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICaptureView](topic13347.md)
    Dim env As [ICaptureViewEnvironment](topic13353.md)
     
    instance.Initialize(env)  
  
C#|   
---|---  
      
    
    void Initialize( 
       [ICaptureViewEnvironment](topic13353.md) _env_
    )  
  
#### Parameters

 _env_
    The environment of the view.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICaptureView Interface](topic13347.md)   
[ICaptureView Members](topic13348.md)


