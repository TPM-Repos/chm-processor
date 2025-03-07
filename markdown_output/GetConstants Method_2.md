Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetConstants Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstants Class](topic4246.md) : GetConstants Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all the constants which exist in the project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetConstants() As [ProjectConstant()](topic4171.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstants](topic4246.md)
    Dim value() As [ProjectConstant](topic4171.md)
     
    value = instance.GetConstants()  
  
C#|   
---|---  
      
    
    public abstract [ProjectConstant[]](topic4171.md) GetConstants()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectConstants Class](topic4246.md)   
[ProjectConstants Members](topic4247.md)


