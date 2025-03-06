![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VariableEventArgs Constructor(ProjectVariable)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5881.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [VariableEventArgs Class](topic5874.md) > [VariableEventArgs Constructor](topic5880.md) : VariableEventArgs Constructor(ProjectVariable)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_variable_
    The variable that was changed.

Glossary Item Box

Initializes a new instance of the [VariableEventArgs](topic5874.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _variable_ As [ProjectVariable](topic4927.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim variable As [ProjectVariable](topic4927.md)
     
    Dim instance As New [VariableEventArgs](topic5874.md)(variable)  
  
C#|   
---|---  
      
    
    public VariableEventArgs( 
       [ProjectVariable](topic4927.md) _variable_
    )  
  
#### Parameters

 _variable_
    The variable that was changed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[VariableEventArgs Class](topic5874.md)   
[VariableEventArgs Members](topic5875.md)   
[Overload List](topic5880.md)

©2024 DriveWorks Ltd. All Rights Reserved.
