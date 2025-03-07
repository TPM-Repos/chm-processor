Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetParameters Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileFormatGenerator Class](topic13579.md) : GetParameters Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_capturedSolidWorksComponent_
    The component to get valid parameters for.

Glossary Item Box

Gets all parameters that should be captured for a particular component. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable Function GetParameters( _
       ByVal _capturedSolidWorksComponent_ As [CapturedSolidWorksComponent](topic14343.md) _
    ) As [FileFormatParameterInfo()](topic13615.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FileFormatGenerator](topic13579.md)
    Dim capturedSolidWorksComponent As [CapturedSolidWorksComponent](topic14343.md)
    Dim value() As [FileFormatParameterInfo](topic13615.md)
     
    value = instance.GetParameters(capturedSolidWorksComponent)  
  
C#|   
---|---  
      
    
    public virtual [FileFormatParameterInfo[]](topic13615.md) GetParameters( 
       [CapturedSolidWorksComponent](topic14343.md) _capturedSolidWorksComponent_
    )  
  
#### Parameters

 _capturedSolidWorksComponent_
    The component to get valid parameters for.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileFormatGenerator Class](topic13579.md)   
[FileFormatGenerator Members](topic13580.md)


