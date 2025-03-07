Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Items Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [VirtualItemsRequestEventArgs Class](topic1192.md) : Items Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the virtual items which will be used by the sender of the event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Items As [VirtualItemData()](topic1154.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [VirtualItemsRequestEventArgs](topic1192.md)
    Dim value() As [VirtualItemData](topic1154.md)
     
    instance.Items = value
     
    value = instance.Items  
  
C#|   
---|---  
      
    
    public [VirtualItemData[]](topic1154.md) Items {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[VirtualItemsRequestEventArgs Class](topic1192.md)   
[VirtualItemsRequestEventArgs Members](topic1193.md)


