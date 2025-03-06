![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetIsDynamic Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6639.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskProperty Class](topic6633.md) : SetIsDynamic Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_isDynamic_
    True if this property should be bound to a rule, False for it to be bound to a static value.

Glossary Item Box

Changes whether this property is bound to a rule, or a static value. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetIsDynamic( _
       ByVal _isDynamic_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskProperty](topic6633.md)
    Dim isDynamic As Boolean
     
    instance.SetIsDynamic(isDynamic)  
  
C#|   
---|---  
      
    
    public void SetIsDynamic( 
       bool _isDynamic_
    )  
  
#### Parameters

 _isDynamic_
    True if this property should be bound to a rule, False for it to be bound to a static value.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| The property does not support being made dynamic.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ComponentTaskProperty Class](topic6633.md)   
[ComponentTaskProperty Members](topic6634.md)

©2024 DriveWorks Ltd. All Rights Reserved.
