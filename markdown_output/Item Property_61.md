Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskConditions Class](topic6561.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the item to get.

Glossary Item Box

Gets the item at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ComponentTaskCondition](topic6493.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskConditions](topic6561.md)
    Dim index As Integer
    Dim value As [ComponentTaskCondition](topic6493.md)
     
    instance.Item(index) = value
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ComponentTaskCondition](topic6493.md) this[ 
       int _index_
    ]; {get; set;}  
  
#### Parameters

 _index_
    The index of the item to get.

#### Property Value

The condition at the specified index.

# Exceptions

Exception| Description  
---|---  
System.ArgumentOutOfRangeException| Index is not a valid index for the collection.  
System.NotSupportedException| Attempting to call the setter of this property.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskConditions Class](topic6561.md)   
[ComponentTaskConditions Members](topic6562.md)


