       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VirtualItemSelectedEventArgs Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [VirtualItemSelectedEventArgs Class](topic1184.md) : VirtualItemSelectedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_item_
    The data for the virtual item that was selected.

Glossary Item Box

Initializes a new instance of the [VirtualItemSelectedEventArgs](topic1184.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _item_ As [VirtualItemData](topic1154.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[VirtualItemSelectedEventArgs Class](topic1184.md)   
[VirtualItemSelectedEventArgs Members](topic1185.md)


