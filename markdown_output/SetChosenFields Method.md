![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetChosenFields Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5407.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SqlServerDataTable Class](topic5396.md) : SetChosenFields Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fieldsToSet_
    

Glossary Item Box

Sets the chosen fields for this table. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetChosenFields( _
       ByVal _fieldsToSet_() As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [SqlServerDataTable](topic5396.md)
    Dim fieldsToSet() As String
     
    instance.SetChosenFields(fieldsToSet)  
  
C#|   
---|---  
      
    
    public void SetChosenFields( 
       string[] _fieldsToSet_
    )  
  
#### Parameters

 _fieldsToSet_
    

# ![](dotnetimages/collapse.gif)Remarks

Will set [AllFields](topic5408.md) to false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SqlServerDataTable Class](topic5396.md)   
[SqlServerDataTable Members](topic5397.md)

©2024 DriveWorks Ltd. All Rights Reserved.
