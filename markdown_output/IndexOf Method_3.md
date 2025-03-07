Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IndexOf Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskConditions Class](topic6561.md) : IndexOf Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_item_
    The condition to locate in the collection.

Glossary Item Box

Determines the index of the specific condition in the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function IndexOf( _
       ByVal _item_ As [ComponentTaskCondition](topic6493.md) _
    ) As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskConditions](topic6561.md)
    Dim item As [ComponentTaskCondition](topic6493.md)
    Dim value As Integer
     
    value = instance.IndexOf(item)  
  
C#|   
---|---  
      
    
    public int IndexOf( 
       [ComponentTaskCondition](topic6493.md) _item_
    )  
  
#### Parameters

 _item_
    The condition to locate in the collection.

#### Return Value

The index of condition if found in the collection, otherwise -1.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskConditions Class](topic6561.md)   
[ComponentTaskConditions Members](topic6562.md)


