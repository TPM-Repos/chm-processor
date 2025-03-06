![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreviewResourceChangedEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3825.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [PreviewResourceChangedEventArgs Class](topic3819.md) : PreviewResourceChangedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_resourceName_
    The name of 3D Preview's resource which has changed.

Glossary Item Box

Event args for when a 3D Preview's resource has been changed. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _resourceName_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim resourceName As String
     
    Dim instance As New [PreviewResourceChangedEventArgs](topic3819.md)(resourceName)  
  
C#|   
---|---  
      
    
    public PreviewResourceChangedEventArgs( 
       string _resourceName_
    )  
  
#### Parameters

 _resourceName_
    The name of 3D Preview's resource which has changed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[PreviewResourceChangedEventArgs Class](topic3819.md)   
[PreviewResourceChangedEventArgs Members](topic3820.md)

©2024 DriveWorks Ltd. All Rights Reserved.
