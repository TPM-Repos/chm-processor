![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyNameChanged Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7104.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [NodeOutputCollection Class](topic7087.md) : NotifyNameChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_endpoint_
    

_oldName_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub NotifyNameChanged( _
       ByVal _endpoint_ As [ConnectionEndpoint](topic6918.md), _
       ByVal _oldName_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [NodeOutputCollection](topic7087.md)
    Dim endpoint As [ConnectionEndpoint](topic6918.md)
    Dim oldName As String
     
    instance.NotifyNameChanged(endpoint, oldName)  
  
C#|   
---|---  
      
    
    public void NotifyNameChanged( 
       [ConnectionEndpoint](topic6918.md) _endpoint_ ,
       string _oldName_
    )  
  
#### Parameters

 _endpoint_
    
_oldName_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[NodeOutputCollection Class](topic7087.md)   
[NodeOutputCollection Members](topic7088.md)

©2024 DriveWorks Ltd. All Rights Reserved.
