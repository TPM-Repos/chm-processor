       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UnparsableFlowPropertyValueException Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11812.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [UnparsableFlowPropertyValueException Class](topic11805.md) : UnparsableFlowPropertyValueException Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the property.

_value_
    The value that was given.

_type_
    The expected type.

Glossary Item Box

Creates a new instance of the [UnparsableFlowPropertyValueException](topic11805.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _name_ As String, _
       ByVal _value_ As String, _
       ByVal _type_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim name As String
    Dim value As String
    Dim type As String
     
    Dim instance As New [UnparsableFlowPropertyValueException](topic11805.md)(name, value, type)  
  
C#|   
---|---  
      
    
    public UnparsableFlowPropertyValueException( 
       string _name_ ,
       string _value_ ,
       string _type_
    )  
  
#### Parameters

 _name_
    The name of the property.
_value_
    The value that was given.
_type_
    The expected type.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[UnparsableFlowPropertyValueException Class](topic11805.md)   
[UnparsableFlowPropertyValueException Members](topic11806.md)

©2024 DriveWorks Ltd. All Rights Reserved.
