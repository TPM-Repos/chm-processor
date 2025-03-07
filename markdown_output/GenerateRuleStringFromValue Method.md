Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GenerateRuleStringFromValue Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) : GenerateRuleStringFromValue Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value of the static property to be converted.

Glossary Item Box

Converts the value of a static property into a dynamic rule string. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GenerateRuleStringFromValue( _
       ByVal _value_ As Object _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim value As Object
    Dim value As String
     
    value = instance.GenerateRuleStringFromValue(value)  
  
C#|   
---|---  
      
    
    public string GenerateRuleStringFromValue( 
       object _value_
    )  
  
#### Parameters

 _value_
    The value of the static property to be converted.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)


