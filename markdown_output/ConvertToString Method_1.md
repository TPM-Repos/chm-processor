Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConvertToString Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [StoreConverter Class](topic9528.md) : ConvertToString Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The source value.

Glossary Item Box

Converts a IArrayValue to a string. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ConvertToString( _
       ByVal _value_ As Titan.Rules.Execution.IArrayValue _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim value As Titan.Rules.Execution.IArrayValue
    Dim value As Object
     
    value = [StoreConverter](topic9528.md).ConvertToString(value)  
  
C#|   
---|---  
      
    
    public static object ConvertToString( 
       Titan.Rules.Execution.IArrayValue _value_
    )  
  
#### Parameters

 _value_
    The source value.

#### Return Value

A string.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StoreConverter Class](topic9528.md)   
[StoreConverter Members](topic9529.md)


