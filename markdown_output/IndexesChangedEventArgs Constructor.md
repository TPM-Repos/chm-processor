![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IndexesChangedEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3502.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IndexesChangedEventArgs Class](topic3496.md) : IndexesChangedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_changedIndexes_
    The original index.

Glossary Item Box

Creates a new instance of the [IndexesChangedEventArgs](topic3496.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _changedIndexes_ As IEnumerable(Of ChangedValue(Of Integer)) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim changedIndexes As IEnumerable(Of ChangedValue(Of Integer))
     
    Dim instance As New [IndexesChangedEventArgs](topic3496.md)(changedIndexes)  
  
C#|   
---|---  
      
    
    public IndexesChangedEventArgs( 
       IEnumerable<ChangedValue<int>> _changedIndexes_
    )  
  
#### Parameters

 _changedIndexes_
    The original index.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IndexesChangedEventArgs Class](topic3496.md)   
[IndexesChangedEventArgs Members](topic3497.md)

©2024 DriveWorks Ltd. All Rights Reserved.
