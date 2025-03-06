![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ToArray(Boolean) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11750.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Teams Class](topic11737.md) > [ToArray Method](topic11748.md) : ToArray(Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_includePermissions_
    True to include !, ?, * in the returned array if the associated permissions are set, false to return only team information.

Glossary Item Box

Copies all of the team identifiers to a new array and returns them. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function ToArray( _
       ByVal _includePermissions_ As Boolean _
    ) As String()  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Teams](topic11737.md)
    Dim includePermissions As Boolean
    Dim value() As String
     
    value = instance.ToArray(includePermissions)  
  
C#|   
---|---  
      
    
    public string[] ToArray( 
       bool _includePermissions_
    )  
  
#### Parameters

 _includePermissions_
    True to include !, ?, * in the returned array if the associated permissions are set, false to return only team information.

#### Return Value

An array of team identifiers represented as strings.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Teams Class](topic11737.md)   
[Teams Members](topic11738.md)   
[Overload List](topic11748.md)

©2024 DriveWorks Ltd. All Rights Reserved.
