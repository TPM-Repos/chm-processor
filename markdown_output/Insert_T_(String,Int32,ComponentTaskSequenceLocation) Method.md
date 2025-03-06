![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

_T_
    The type of the task to create.

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Insert<T>(String,Int32,ComponentTaskSequenceLocation) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskAccessor Class](topic6429.md) > [Insert Method](topic6445.md) : Insert<T>(String,Int32,ComponentTaskSequenceLocation) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the task to create.

_index_
    The index to insert the newly created task in.

_location_
    The location of the task to insert.

Glossary Item Box

Creates and inserts a new [ComponentTask](topic6407.md) at the given index. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Insert(Of T)( _
       ByVal _name_ As String, _
       ByVal _index_ As Integer, _
       ByVal _location_ As [ComponentTaskSequenceLocation](topic6406.md) _
    ) As [ComponentTask](topic6407.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskAccessor](topic6429.md)
    Dim name As String
    Dim index As Integer
    Dim location As [ComponentTaskSequenceLocation](topic6406.md)
    Dim value As [ComponentTask](topic6407.md)
     
    value = instance.Insert(Of T)(name, index, location)  
  
C#|   
---|---  
      
    
    public [ComponentTask](topic6407.md) Insert<T>( 
       string _name_ ,
       int _index_ ,
       [ComponentTaskSequenceLocation](topic6406.md) _location_
    )  
  
#### Parameters

 _name_
    The name of the task to create.
_index_
    The index to insert the newly created task in.
_location_
    The location of the task to insert.

#### Type Parameters

_T_
    The type of the task to create.

#### Return Value

The newly created task, or a null reference (Nothing in VB) if the creation of the task fails.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.IndexOutOfRangeException| Index is negative or greater than the size of the collection.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ComponentTaskAccessor Class](topic6429.md)   
[ComponentTaskAccessor Members](topic6430.md)   
[Overload List](topic6445.md)


