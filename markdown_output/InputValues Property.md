Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InputValues Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [SpecificationHostControl Class](topic8979.md) : InputValues Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

An optional table that has two columns (Name and Value). The values will be driven into the hosted specification based on the name column. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property InputValues As [ITableValue](topic2331.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationHostControl](topic8979.md)
    Dim value As [ITableValue](topic2331.md)
     
    instance.InputValues = value
     
    value = instance.InputValues  
  
C#|   
---|---  
      
    
    public [ITableValue](topic2331.md) InputValues {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationHostControl Class](topic8979.md)   
[SpecificationHostControl Members](topic8980.md)


