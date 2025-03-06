![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProposeNewControlName(String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7781.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlCollection Class](topic7766.md) > [ProposeNewControlName Method](topic7780.md) : ProposeNewControlName(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_currentControlName_
    The current name of the control.

Glossary Item Box

Proposes a new control name, for example in a copy and paste operation. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function ProposeNewControlName( _
       ByVal _currentControlName_ As String _
    ) As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ControlCollection](topic7766.md)
    Dim currentControlName As String
    Dim value As String
     
    value = instance.ProposeNewControlName(currentControlName)  
  
C#|   
---|---  
      
    
    public string ProposeNewControlName( 
       string _currentControlName_
    )  
  
#### Parameters

 _currentControlName_
    The current name of the control.

#### Return Value

A new control name, optionally suffixed with an index which makes the name unique.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ControlCollection Class](topic7766.md)   
[ControlCollection Members](topic7767.md)   
[Overload List](topic7780.md)

©2024 DriveWorks Ltd. All Rights Reserved.
