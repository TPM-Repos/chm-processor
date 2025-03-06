![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VirtualItemSelectedEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1190.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [VirtualItemSelectedEventArgs Class](topic1184.md) : VirtualItemSelectedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_item_
    The data for the virtual item that was selected.

Glossary Item Box

Initializes a new instance of the [VirtualItemSelectedEventArgs](topic1184.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _item_ As [VirtualItemData](topic1154.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim item As [VirtualItemData](topic1154.md)
     
    Dim instance As New [VirtualItemSelectedEventArgs](topic1184.md)(item)  
  
C#|   
---|---  
      
    
    public VirtualItemSelectedEventArgs( 
       [VirtualItemData](topic1154.md) _item_
    )  
  
#### Parameters

 _item_
    The data for the virtual item that was selected.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[VirtualItemSelectedEventArgs Class](topic1184.md)   
[VirtualItemSelectedEventArgs Members](topic1185.md)

©2024 DriveWorks Ltd. All Rights Reserved.
