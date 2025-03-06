![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UpdatePlaceholderData Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5252.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RollupDataTable Class](topic5240.md) : UpdatePlaceholderData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newData_
    The new placeholder data. If Nothing or an empty 2D array is passed in then this will clear the data.

Glossary Item Box

Updates the placeholder data with the new values. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub UpdatePlaceholderData( _
       ByVal _newData_(,) As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RollupDataTable](topic5240.md)
    Dim newData() As String
     
    instance.UpdatePlaceholderData(newData)  
  
C#|   
---|---  
      
    
    public void UpdatePlaceholderData( 
       string[,] _newData_
    )  
  
#### Parameters

 _newData_
    The new placeholder data. If Nothing or an empty 2D array is passed in then this will clear the data.

# ![](dotnetimages/collapse.gif)Remarks

If the number of columns in the new data doesn't match the number of columns set for this table then an System.ArgumentException will be thrown.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RollupDataTable Class](topic5240.md)   
[RollupDataTable Members](topic5241.md)

©2024 DriveWorks Ltd. All Rights Reserved.
