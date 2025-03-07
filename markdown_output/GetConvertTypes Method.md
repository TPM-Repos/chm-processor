Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetConvertTypes Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ICanConvert Interface](topic7268.md) : GetConvertTypes Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Returns an array of types that this control can be converted to. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetConvertTypes() As Type()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICanConvert](topic7268.md)
    Dim value() As Type
     
    value = instance.GetConvertTypes()  
  
C#|   
---|---  
      
    
    Type[] GetConvertTypes()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICanConvert Interface](topic7268.md)   
[ICanConvert Members](topic7269.md)


