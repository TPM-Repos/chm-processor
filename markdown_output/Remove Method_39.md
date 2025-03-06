Remove Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskReleaseConditions Class](topic6682.md) : Remove Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_item_
    The item to remove.

Glossary Item Box

Removes the first occurrence of the given condition within the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Remove( _
       ByVal _item_ As [ComponentTaskReleaseCondition](topic6647.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskReleaseConditions](topic6682.md)
    Dim item As [ComponentTaskReleaseCondition](topic6647.md)
    Dim value As Boolean
     
    value = instance.Remove(item)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [ComponentTaskReleaseCondition](topic6647.md) _item_
    )  
  
#### Parameters

 _item_
    The item to remove.

#### Return Value

True if the item was successfully removed, otherwise False.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskReleaseConditions Class](topic6682.md)   
[ComponentTaskReleaseConditions Members](topic6683.md)


