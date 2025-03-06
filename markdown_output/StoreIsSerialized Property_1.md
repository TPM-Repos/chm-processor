StoreIsSerialized Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RollupDataTable Class](topic5240.md) : StoreIsSerialized Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets whether the store should be serialized. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides NotOverridable ReadOnly Property StoreIsSerialized As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RollupDataTable](topic5240.md)
    Dim value As Boolean
     
    value = instance.StoreIsSerialized  
  
C#|   
---|---  
      
    
    protected override bool StoreIsSerialized {get;}  
  
# Remarks

This will always return false as the data should only ever be kept in-memory.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RollupDataTable Class](topic5240.md)   
[RollupDataTable Members](topic5241.md)


