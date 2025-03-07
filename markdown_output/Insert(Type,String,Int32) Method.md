Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Insert(Type,String,Int32) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskAccessor Class](topic6429.md) > [Insert Method](topic6445.md) : Insert(Type,String,Int32) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_type_
    The type of the task to create.

_name_
    The name of the task to create.

_index_
    The index to insert the newly created task in.

Glossary Item Box

Creates and inserts a new [ComponentTask](topic6407.md) at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Insert( _
       ByVal _type_ As Type, _
       ByVal _name_ As String, _
       ByVal _index_ As Integer _
    ) As [ComponentTask](topic6407.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskAccessor](topic6429.md)
    Dim type As Type
    Dim name As String
    Dim index As Integer
    Dim value As [ComponentTask](topic6407.md)
     
    value = instance.Insert(type, name, index)  
  
C#|   
---|---  
      
    
    public [ComponentTask](topic6407.md) Insert( 
       Type _type_ ,
       string _name_ ,
       int _index_
    )  
  
#### Parameters

 _type_
    The type of the task to create.
_name_
    The name of the task to create.
_index_
    The index to insert the newly created task in.

#### Return Value

The newly created task, or a null reference (Nothing in VB) if the creation of the task fails.

# Exceptions

Exception| Description  
---|---  
System.IndexOutOfRangeException| Index is negative or greater than the size of the collection.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskAccessor Class](topic6429.md)   
[ComponentTaskAccessor Members](topic6430.md)   
[Overload List](topic6445.md)


