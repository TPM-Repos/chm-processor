![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetData Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3493.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ImportedDataTable Class](topic3483.md) : SetData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_data_
    The new data to place in the table.

Glossary Item Box

Set the data for this table. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetData( _
       ByVal _data_(,) As Object _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ImportedDataTable](topic3483.md)
    Dim data() As Object
     
    instance.SetData(data)  
  
C#|   
---|---  
      
    
    public void SetData( 
       object[,] _data_
    )  
  
#### Parameters

 _data_
    The new data to place in the table.

# ![](dotnetimages/collapse.gif)Remarks

Previous values will be lost

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ImportedDataTable Class](topic3483.md)   
[ImportedDataTable Members](topic3484.md)

©2024 DriveWorks Ltd. All Rights Reserved.
