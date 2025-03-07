Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterAnyProperty(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [FlowProperties Class](topic10905.md) > [RegisterAnyProperty Method](topic10911.md) : RegisterAnyProperty(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the property.

Glossary Item Box

Creates a new specification flow property which can store any data. Static values will always be represented as strings. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function RegisterAnyProperty( _
       ByVal _name_ As String _
    ) As [FlowProperty(Of Object)](topic10978.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowProperties](topic10905.md)
    Dim name As String
    Dim value As [FlowProperty(Of Object)](topic10978.md)
     
    value = instance.RegisterAnyProperty(name)  
  
C#|   
---|---  
      
    
    public [FlowProperty<object>](topic10978.md) RegisterAnyProperty( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the property.

#### Return Value

A new specification flow property.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowProperties Class](topic10905.md)   
[FlowProperties Members](topic10906.md)   
[Overload List](topic10911.md)


