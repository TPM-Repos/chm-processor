![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add(Type,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskConditions Class](topic6561.md) > [Add Method](topic6568.md) : Add(Type,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_type_
    The type of the condition to add (Must inherit from [ComponentTaskCondition](topic6493.md)).

_title_
    The title of the condition to create.

Glossary Item Box

Creates and adds a new condition of the specified type to the collection. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Add( _
       ByVal _type_ As Type, _
       ByVal _title_ As String _
    ) As [ComponentTaskCondition](topic6493.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskConditions](topic6561.md)
    Dim type As Type
    Dim title As String
    Dim value As [ComponentTaskCondition](topic6493.md)
     
    value = instance.Add(type, title)  
  
C#|   
---|---  
      
    
    public [ComponentTaskCondition](topic6493.md) Add( 
       Type _type_ ,
       string _title_
    )  
  
#### Parameters

 _type_
    The type of the condition to add (Must inherit from [ComponentTaskCondition](topic6493.md)).
_title_
    The title of the condition to create.

#### Return Value

The newly created condition.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.ArgumentException| The specified type is not a valid [ComponentTaskCondition](topic6493.md) type.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ComponentTaskConditions Class](topic6561.md)   
[ComponentTaskConditions Members](topic6562.md)   
[Overload List](topic6568.md)


