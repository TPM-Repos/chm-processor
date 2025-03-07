Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetConstants Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstantCategories Class](topic4202.md) : GetConstants Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all the constants which haven't been registered with a specific category. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetConstants() As [ProjectConstant()](topic4171.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstantCategories](topic4202.md)
    Dim value() As [ProjectConstant](topic4171.md)
     
    value = instance.GetConstants()  
  
C#|   
---|---  
      
    
    public [ProjectConstant[]](topic4171.md) GetConstants()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectConstantCategories Class](topic4202.md)   
[ProjectConstantCategories Members](topic4203.md)


