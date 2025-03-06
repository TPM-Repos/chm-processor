![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemapComponents Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3047.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupCapturedComponents Class](topic3022.md) : RemapComponents Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldBasePath_
    The base path from which all changes must match.

_newBasePath_
    The new base path to give all matching components.

Glossary Item Box

Attempts to change all captured components and their references that match oldBasePath to use the new base path in newBasePath. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function RemapComponents( _
       ByVal _oldBasePath_ As String, _
       ByVal _newBasePath_ As String _
    ) As IReadOnlyDictionary(Of String,String)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupCapturedComponents](topic3022.md)
    Dim oldBasePath As String
    Dim newBasePath As String
    Dim value As IReadOnlyDictionary(Of String,String)
     
    value = instance.RemapComponents(oldBasePath, newBasePath)  
  
C#|   
---|---  
      
    
    public IReadOnlyDictionary<string,string> RemapComponents( 
       string _oldBasePath_ ,
       string _newBasePath_
    )  
  
#### Parameters

 _oldBasePath_
    The base path from which all changes must match.
_newBasePath_
    The new base path to give all matching components.

#### Return Value

A mapping of all old paths to new paths.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupCapturedComponents Class](topic3022.md)   
[GroupCapturedComponents Members](topic3023.md)

©2024 DriveWorks Ltd. All Rights Reserved.
