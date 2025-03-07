Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Register(String,String,Type) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [NodeOutputCollection Class](topic7087.md) > [Register Method](topic7105.md) : Register(String,String,Type) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the output to create.

_description_
    The user-friendly description of the output.

_valueType_
    The type of the value this output stores.

Glossary Item Box

Adds a new output to the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Register( _
       ByVal _name_ As String, _
       ByVal _description_ As String, _
       ByVal _valueType_ As Type _
    ) As [NodeOutput](topic7074.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NodeOutputCollection](topic7087.md)
    Dim name As String
    Dim description As String
    Dim valueType As Type
    Dim value As [NodeOutput](topic7074.md)
     
    value = instance.Register(name, description, valueType)  
  
C#|   
---|---  
      
    
    public [NodeOutput](topic7074.md) Register( 
       string _name_ ,
       string _description_ ,
       Type _valueType_
    )  
  
#### Parameters

 _name_
    The name of the output to create.
_description_
    The user-friendly description of the output.
_valueType_
    The type of the value this output stores.

#### Return Value

The newly created output.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NodeOutputCollection Class](topic7087.md)   
[NodeOutputCollection Members](topic7088.md)   
[Overload List](topic7105.md)


