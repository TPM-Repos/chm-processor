Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InvalidNumberHandling Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) : InvalidNumberHandling Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets how invalid values (such as System.Double) are treated in this property. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property InvalidNumberHandling As [InvalidNumberHandling](topic9382.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DynamicProperty](topic9398.md)
    Dim value As [InvalidNumberHandling](topic9382.md)
     
    value = instance.InvalidNumberHandling  
  
C#|   
---|---  
      
    
    public [InvalidNumberHandling](topic9382.md) InvalidNumberHandling {get;}  
  
# Remarks

This only applies to property values of type System.Double. Note that System.Double is also covered.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)


