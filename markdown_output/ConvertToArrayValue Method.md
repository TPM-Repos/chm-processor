Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConvertToArrayValue Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [StoreConverter Class](topic9528.md) : ConvertToArrayValue Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The source value.

Glossary Item Box

Converts the specified string to a IArrayValue. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ConvertToArrayValue( _
       ByVal _value_ As String _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim value As String
    Dim value As Object
     
    value = [StoreConverter](topic9528.md).ConvertToArrayValue(value)  
  
C#|   
---|---  
      
    
    public static object ConvertToArrayValue( 
       string _value_
    )  
  
#### Parameters

 _value_
    The source value.

#### Return Value

A IArrayValue.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StoreConverter Class](topic9528.md)   
[StoreConverter Members](topic9529.md)


