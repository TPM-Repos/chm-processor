![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FileFormatParameterInfo Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13621.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileFormatParameterInfo Class](topic13615.md) : FileFormatParameterInfo Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The human readable name of the parameter

_invariantName_
    The unique invariant identifier for the parameter.

Glossary Item Box

Creates a new instance of the [FileFormatParameterInfo](topic13615.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _displayName_ As String, _
       ByVal _invariantName_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim displayName As String
    Dim invariantName As String
     
    Dim instance As New [FileFormatParameterInfo](topic13615.md)(displayName, invariantName)  
  
C#|   
---|---  
      
    
    public FileFormatParameterInfo( 
       string _displayName_ ,
       string _invariantName_
    )  
  
#### Parameters

 _displayName_
    The human readable name of the parameter
 _invariantName_
    The unique invariant identifier for the parameter.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FileFormatParameterInfo Class](topic13615.md)   
[FileFormatParameterInfo Members](topic13616.md)

©2024 DriveWorks Ltd. All Rights Reserved.
