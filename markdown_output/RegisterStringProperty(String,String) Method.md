       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterStringProperty(String,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [FlowProperties Class](topic10905.md) > [RegisterStringProperty Method](topic10940.md) : RegisterStringProperty(String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the property.

_description_
    The description of the property.

Glossary Item Box

Creates a new specification flow property which can store string data. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function RegisterStringProperty( _
       ByVal _name_ As String, _
       ByVal _description_ As String _
    ) As [FlowProperty(Of String)](topic10978.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowProperties](topic10905.md)
    Dim name As String
    Dim description As String
    Dim value As [FlowProperty(Of String)](topic10978.md)
     
    value = instance.RegisterStringProperty(name, description)  
  
C#|   
---|---  
      
    
    public [FlowProperty<string>](topic10978.md) RegisterStringProperty( 
       string _name_ ,
       string _description_
    )  
  
#### Parameters

 _name_
    The name of the property.
_description_
    The description of the property.

#### Return Value

A new specification flow property.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowProperties Class](topic10905.md)   
[FlowProperties Members](topic10906.md)   
[Overload List](topic10940.md)


