Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PropertyTypes Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicPropertyData Class](topic9456.md) : PropertyTypes Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The semantic types that apply to the property. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property PropertyTypes As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DynamicPropertyData](topic9456.md)
    Dim value() As String
     
    instance.PropertyTypes = value
     
    value = instance.PropertyTypes  
  
C#|   
---|---  
      
    
    public string[] PropertyTypes {get; set;}  
  
# Remarks

See [DriveWorks.StandardRuleTypes](topic5461.md) for typical values.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DynamicPropertyData Class](topic9456.md)   
[DynamicPropertyData Members](topic9457.md)


