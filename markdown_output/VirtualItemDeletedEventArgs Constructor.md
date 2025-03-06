       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VirtualItemDeletedEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1173.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [VirtualItemDeletedEventArgs Class](topic1167.md) : VirtualItemDeletedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_item_
    The data for the virtual item that was selected.

Glossary Item Box

Initializes a new instance of the [VirtualItemDeletedEventArgs](topic1167.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _item_ As [VirtualItemData](topic1154.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim item As [VirtualItemData](topic1154.md)
     
    Dim instance As New [VirtualItemDeletedEventArgs](topic1167.md)(item)  
  
C#|   
---|---  
      
    
    public VirtualItemDeletedEventArgs( 
       [VirtualItemData](topic1154.md) _item_
    )  
  
#### Parameters

 _item_
    The data for the virtual item that was selected.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[VirtualItemDeletedEventArgs Class](topic1167.md)   
[VirtualItemDeletedEventArgs Members](topic1168.md)

©2024 DriveWorks Ltd. All Rights Reserved.
