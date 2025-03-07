Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConverterOverride Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicPropertyData Class](topic9456.md) : ConverterOverride Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/Sets an overridden mechanism for converting values to and from their native representation in the backing store. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property ConverterOverride As [IPropertyValueConverter](topic9373.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DynamicPropertyData](topic9456.md)
    Dim value As [IPropertyValueConverter](topic9373.md)
     
    instance.ConverterOverride = value
     
    value = instance.ConverterOverride  
  
C#|   
---|---  
      
    
    public [IPropertyValueConverter](topic9373.md) ConverterOverride {get; set;}  
  
# Remarks

This can for instance be used to add null handling to a type which would not typically support it.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DynamicPropertyData Class](topic9456.md)   
[DynamicPropertyData Members](topic9457.md)


